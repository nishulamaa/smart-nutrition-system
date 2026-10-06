const API_URL = "http://127.0.0.1:8000";


// =========================
// IMAGE PREVIEW
// =========================

const imageInput =
    document.getElementById("foodImage");

const imagePreview =
    document.getElementById("imagePreview");


imageInput.addEventListener(
    "change",
    function () {

        const file = this.files[0];

        if (!file) {

            imagePreview.style.display = "none";

            imagePreview.innerHTML = "";

            return;
        }


        const reader =
            new FileReader();


        reader.onload = function (event) {

            imagePreview.innerHTML = `

                <img
                    src="${event.target.result}"
                    alt="Selected food"
                >

            `;

            imagePreview.style.display = "block";

        };


        reader.readAsDataURL(file);

    }
);



// =========================
// ANALYZE FOOD
// =========================

async function analyzeFood() {

    const imageInput =
        document.getElementById("foodImage");

    const budget =
        document.getElementById("budget").value;

    const timeLimit =
        document.getElementById("timeLimit").value;

    const preference =
        document.getElementById("preference").value;

    const result =
        document.getElementById("result");

    const loading =
        document.getElementById("loading");


    // Validation

    if (!budget || !timeLimit) {

        result.innerHTML = `

            <div class="empty-result">

                <div>⚠️</div>

                <p>
                    Please enter your budget
                    and available time.
                </p>

            </div>

        `;

        return;
    }



    // FormData

    const formData =
        new FormData();


    if (imageInput.files.length > 0) {

        formData.append(
            "file",
            imageInput.files[0]
        );

    }


    formData.append(
        "budget",
        budget
    );


    formData.append(
        "time_limit",
        timeLimit
    );


    formData.append(
        "preference",
        preference
    );



    // Loading

    loading.classList.remove("hidden");

    result.innerHTML = "";



    try {

        const response =
            await fetch(
                `${API_URL}/api/analyze-food`,
                {
                    method: "POST",
                    body: formData
                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Request failed"
            );

        }



        // Display result

        result.innerHTML = `

            <h3>
                ${data.food_name}
            </h3>


            <div class="result-grid">


                <div class="result-item">

                    <strong>
                        ${data.calories}
                    </strong>

                    <span>
                        Calories
                    </span>

                </div>


                <div class="result-item">

                    <strong>
                        ${data.protein}g
                    </strong>

                    <span>
                        Protein
                    </span>

                </div>


                <div class="result-item">

                    <strong>
                        ${data.carbs}g
                    </strong>

                    <span>
                        Carbohydrates
                    </span>

                </div>


                <div class="result-item">

                    <strong>
                        ₩${Number(
                            data.price
                        ).toLocaleString("ko-KR")}
                    </strong>

                    <span>
                        Price
                    </span>

                </div>

            </div>


            <p>

                <strong>
                    Preparation time:
                </strong>

                ${data.preparation_time}
                minutes

            </p>


            <div class="reason">

                <strong>
                    Why this meal?
                </strong>

                <br>

                ${data.recommendation_reason}

            </div>

        `;



        // Scroll to result

        document
            .getElementById("recommendation")
            .scrollIntoView({
                behavior: "smooth"
            });


    } catch (error) {

        console.error(error);


        result.innerHTML = `

            <div class="empty-result">

                <div>
                    ❌
                </div>

                <p>
                    Could not connect to
                    the NutriSmart backend.
                </p>

                <small>
                    Make sure FastAPI is running
                    on http://127.0.0.1:8000
                </small>

            </div>

        `;

    } finally {

        loading.classList.add("hidden");

    }

}



// =========================
// LOAD FOOD LIST
// =========================

async function loadFoods() {

    const foodList =
        document.getElementById("foodList");


    try {

        const response =
            await fetch(
                `${API_URL}/api/foods`
            );


        if (!response.ok) {

            throw new Error(
                "Could not load foods"
            );

        }


        const foods =
            await response.json();


        foodList.innerHTML = "";


        foods.forEach(
            function (food) {

                const card =
                    document.createElement(
                        "div"
                    );


                card.className =
                    "food-card";


                card.innerHTML = `

                    <h3>
                        ${food.name}
                    </h3>


                    <p>
                        Calories:
                        ${food.calories} kcal
                    </p>


                    <p>
                        Protein:
                        ${food.protein} g
                    </p>


                    <p>
                        Carbs:
                        ${food.carbs} g
                    </p>


                    <p class="price">
                        ₩${Number(
                            food.price
                        ).toLocaleString("ko-KR")}
                    </p>


                    <p>
                        Preparation:
                        ${food.preparation_time}
                        min
                    </p>

                `;


                foodList.appendChild(card);

            }
        );


    } catch (error) {

        console.error(error);


        foodList.innerHTML = `

            <p>
                Could not load meals.
                Please check whether
                FastAPI is running.
            </p>

        `;

    }

}



// =========================
// START
// =========================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        loadFoods();

    }
);
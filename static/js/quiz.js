

function getQuizContainer(question) {
    const html = `<div id="quiz-section" class="justify-center w-1/2 p-6">
    <!-- Question Section -->
    <div id="question-box" class="bg-black bg-opacity-50 p-6 rounded-lg shadow-lg text-white text-center">
      <h1 class="text-4xl font-bold">Q${currentQuestionIndex + 1}. ${question['question']}</h1>
    </div>
    
    <!-- Options Section -->
    <form id="option-form" class="space-y-6 bg-black bg-opacity-50 p-6 rounded-lg shadow-lg">
      ${question['options'].map((option, index) => {
        return `
        <div class="flex justify-center">
          <input type="radio" class="btn-check" name="options" id="option${index + 1}" value="${option}" autocomplete="off">
          <label class="btn btn-primary block py-3 px-4 rounded-lg cursor-pointer text-white text-center" for="option${index + 1}">
          ${option}
          </label>
        </div>
        `
    }).join('')}
    </form>

    <div class="flex justify-center mt-6">
      <button id="next-button" class="px-6 btn btn-primary btn-lg">
        Next Question
      </button>
    </div>
  </div>`;
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, "text/html");
    return doc.body.firstChild;
}

let currentQuestionIndex = 0;
const questionDuration = 10;
let countdown;

const timerElement = document.getElementById("timer");
const quizContainer = document.getElementById("quiz-container");

function showNextQuestion() {
    if (currentQuestionIndex < QUESTIONS.length) {
        const question = QUESTIONS[currentQuestionIndex];

        quizContainer.innerHTML = "";

        const questionContainer = getQuizContainer(question);

        quizContainer.appendChild(questionContainer);

        startTimer(questionDuration);

        currentQuestionIndex++;
    } else {
        endQuiz();
    }
}

let result = []

function saveAnswer() {
    const question = QUESTIONS[currentQuestionIndex - 1];
    const selectedOption = document.querySelector('input[name="options"]:checked');
    if (selectedOption) {
        const answer = selectedOption.value;
        result.push({
            id: question.id,
            answer: answer
        });
    } else {
        result.push({
            id: question.id,
            answer: null
        });
    }
}

function startTimer(duration) {
    let timeLeft = duration;
    timerElement.textContent = `Time Left: ${timeLeft}s`;

    clearInterval(countdown);

    countdown = setInterval(() => {
        timeLeft--;
        timerElement.textContent = `Time Left: ${timeLeft}s`;

        if (timeLeft <= 0) {
            saveAnswer();
            showNextQuestion();
        }
    }, 1000);
}

function endQuiz() {
    sendResult();
    const pathSegments = window.location.pathname.split('/');
    const uuid = pathSegments[pathSegments.length - 1];
    quizContainer.classList.add("items-center");
    quizContainer.innerHTML = `
        <div class="text-center justify-center w-1/2 p-6">
            <h1 class="text-4xl font-bold mb-4">Quiz Completed! 🎉</h1>
            
            <a href="/quiz/result/${uuid}" class="mt-6 px-6 py-3 bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 text-white font-semibold rounded-lg shadow-md hover:shadow-lg transition duration-300 ease-in-out transform hover:scale-105">
                View Results
            </a>
        </div>
    `;
    timerElement.parentElement.remove();
    clearInterval(countdown);
}
async function sendResult() {
    const pathSegments = window.location.pathname.split('/');
    const uuid = pathSegments[pathSegments.length - 1];

    try {
        const response = await fetch(`/quiz/save-result/${uuid}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': CSRF,
            },
            body: JSON.stringify(result)
        });
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}

showNextQuestion();

document.getElementById("quiz-container").addEventListener("click", (e) => {
    if (e.target && e.target.id === "next-button") {
        e.preventDefault();
        saveAnswer();
        showNextQuestion();
    }
});
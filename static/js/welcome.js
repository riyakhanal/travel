document.addEventListener("DOMContentLoaded", function () {
    let selectedDestinations = [];

    window.toggleSelection = function (element) {
        const destinationName = element.querySelector("p").textContent;

        if (selectedDestinations.includes(destinationName)) {
            selectedDestinations = selectedDestinations.filter(name => name !== destinationName);
            element.classList.remove("selected");
        } else {
            selectedDestinations.push(destinationName);
            element.classList.add("selected");
        }

        // Enable/Disable "Let's Go" button based on selections
        document.getElementById("lets-go-btn").disabled = selectedDestinations.length === 0;
    };

    window.proceed = function () {
        if (selectedDestinations.length > 0) {
            alert("You selected: " + selectedDestinations.join(", "));
            window.location.href = "/nextpage"; // Change this to your actual next page route
        }
    };
});

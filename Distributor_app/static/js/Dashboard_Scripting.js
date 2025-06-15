document.addEventListener("DOMContentLoaded", function () {
    // Get Elements
    const profileContainer = document.getElementById("profile-container");
    const inputFile = document.getElementById("input-file");
    const profilePic = document.getElementById("Profile-Picture");
    const ctx = document.getElementById("userPerformanceChart")?.getContext("2d");
    let userChart;
    const timeFilters = document.querySelectorAll(".time-filter");

    let currentFilter = "month"; // Default view
    let selectedMonth = null; // Store selected month
    let selectedYear = null; // Store selected year

    // 📷 Profile Picture Upload Logic
    if (inputFile && profilePic) {
        profileContainer.addEventListener("click", () => inputFile.click());
        inputFile.addEventListener("change", function () {
            if (inputFile.files.length > 0) {
                const reader = new FileReader();
                reader.onload = (e) => (profilePic.src = e.target.result);
                reader.readAsDataURL(inputFile.files[0]);
            }
        });
    }

    // 📌 Sidebar Menu Logic
    window.ShowSidebar = () => {
        const sidebar = document.querySelector(".sidebar");
        if (sidebar) {
            sidebar.style.display = "flex";
        }
    };
    window.HideSidebar = () => {
        const sidebar = document.querySelector(".sidebar");
        if (sidebar) {
            sidebar.style.display = "none";
        }
    };

    // 🛒 Populate Recent Transactions Table
    function populateRecentTransactions() {
        const transactionBody = document.getElementById("transaction-body");
        if (!transactionBody) return;
        transactionBody.innerHTML = ""; // Clear previous rows

        const cart = JSON.parse(localStorage.getItem("cartKey")) || {};
        const currentDate = new Date().toLocaleDateString();

        let index = 1;
        Object.values(cart).forEach((item) => {
            transactionBody.insertAdjacentHTML(
                "beforeend",
                `<tr>
                    <td>${index}</td>
                    <td>${currentDate}</td>
                    <td>${item.name}</td>
                    <td>${item.quantity}</td>
                    <td>₦${item.price}</td>
                    <td>₦${item.price * item.quantity}</td>
                </tr>`
            );
            index++;
        });
    }

    // 📄 Generate Invoice and Populate Transactions
    const invoiceBtn = document.getElementById("generate-invoice-btn");
    if (invoiceBtn) {
        invoiceBtn.addEventListener("click", populateRecentTransactions);
    }

    // 📊 Fetch & Display User Performance (BAR CHART)
    function fetchUserPerformanceData(filter, month = null, year = null) {
        console.log("Fetching data for filter:", filter);  // Debugging: log filter
        let url = `/dashboard/user-performance/?filter_by=${filter}`;
        
        // Add month and year filters to the URL if applicable
        if (month) url += `&month=${month}`;
        if (year) url += `&year=${year}`;

        fetch(url)
            .then((response) => response.json())
            .then((data) => {
                if (data.error) return console.error("Error:", data.error);

                // Create a darker blue gradient
                const gradient = ctx.createLinearGradient(0, 0, 0, 300);
                gradient.addColorStop(0, "rgba(25, 3, 152, 0.8)");  // Darker shade at the top
                gradient.addColorStop(1, "rgba(54, 62, 235, 0.2)");  // Darker shade at the bottom

                // Destroy previous chart if exists
                if (userChart) userChart.destroy();

                // Create new BAR chart
                userChart = new Chart(ctx, {
                    type: "bar",
                    data: {
                        labels: data.labels,
                        datasets: [
                            {
                                label: "Payments Made",
                                data: data.data,
                                backgroundColor: gradient,
                                borderColor: "rgb(6, 55, 87)",
                                borderWidth: 1,
                                borderRadius: 5, // Rounded corners
                            },
                        ],
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            x: { grid: { display: false } },
                            y: { beginAtZero: true },
                        },
                        plugins: {
                            legend: { display: false }, // Hides the legend
                        },
                    },
                });
            })
            .catch((error) => console.error("Failed to load user data:", error));
    }

    // Fetch default chart on page load
    fetchUserPerformanceData(currentFilter);

    // Add event listeners to filter buttons
    timeFilters.forEach((button) => {
        button.addEventListener("click", function () {
            currentFilter = this.getAttribute("data-filter");
            console.log("Selected filter:", currentFilter);  // Debugging: log selected filter
            
            // Get month and year if needed
            const month = selectedMonth;
            const year = selectedYear;

            fetchUserPerformanceData(currentFilter, month, year);

            // Highlight active filter
            timeFilters.forEach((btn) => btn.classList.remove("active"));
            this.classList.add("active");
        });
    });

    // Example: Logic for setting month and year (modify as per your UI for month/year selection)
    const monthSelector = document.getElementById("month-selector");
    const yearSelector = document.getElementById("year-selector");

    if (monthSelector) {
        monthSelector.addEventListener("change", function () {
            selectedMonth = this.value;
            fetchUserPerformanceData(currentFilter, selectedMonth, selectedYear);
        });
    }

    if (yearSelector) {
        yearSelector.addEventListener("change", function () {
            selectedYear = this.value;
            fetchUserPerformanceData(currentFilter, selectedMonth, selectedYear);
        });
    }
    // Ensure active class toggles correctly
timeFilters.forEach((button) => {
    button.addEventListener("click", function () {
        currentFilter = this.getAttribute("data-filter");
        fetchUserPerformanceData(currentFilter); // Function to update chart

        // Remove 'active' from all buttons and add to the clicked one
        timeFilters.forEach((btn) => btn.classList.remove("active"));
        this.classList.add("active");
    });
});

});

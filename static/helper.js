function setupTabs(){
    document.querySelectorAll(".tabs-buttons").forEach(button => {
        button.addEventListener("click", () =>{
            const sideBar = button.parentElement;
            const tabsContainer = sideBar.parentElement;
            const tabNumber = button.dataset.forTab;
            const tabToActivate = tabsContainer.querySelector(`.tool-options[data-tab="${tabNumber}"]`);

            sideBar.querySelectorAll(".tabs-buttons").forEach(button =>{
                button.classList.remove("tabs-buttons--active");
            });

            tabsContainer.querySelectorAll(".tool-options").forEach(button =>{
                button.classList.remove("tool-options--active");
            });

            button.classList.add("tabs-buttons--active");
            tabToActivate.classList.add("tool-options--active");

        });
    });
}
document.addEventListener("DOMContentLoaded", () => { // When HTML Data loaded class this function
    setupTabs();

    document.querySelectorAll(".tool-box").forEach(tabsContainer => {
        tabsContainer.querySelector(".side-tabs .tabs-buttons").click();
    });
});

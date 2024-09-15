document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".sidenav-btn")
  const sections = document.querySelectorAll("section")

  // Function to hide all sections
  function hideAllSections() {
    sections.forEach((section) => {
      section.style.display = "none"
    })
  }

  // Function to add event listeners to each button
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      hideAllSections() // Hide all sections first
      const sectionId = this.id.replace("-btn", "") // Corresponding section id
      document.getElementById(sectionId).style.display = "flex" // Show the corresponding section
    })
  })

  // Optionally show the first section by default
  document.getElementById("patientinfo").style.display = "block"
})

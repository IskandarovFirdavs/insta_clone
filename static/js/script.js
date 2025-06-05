// Instagram Clone JavaScript - Exact Original Functionality

document.addEventListener("DOMContentLoaded", () => {
  // Like button functionality
  const likeButtons = document.querySelectorAll(".like-btn")
  likeButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const svg = this.querySelector("svg")
      const path = svg.querySelector("path")

      if (svg.getAttribute("fill") === "none") {
        svg.setAttribute("fill", "#ff3040")
        svg.setAttribute("stroke", "#ff3040")
        path.setAttribute("fill", "#ff3040")
        // Add animation
        this.style.animation = "heartPop 0.3s ease-out"
        setTimeout(() => {
          this.style.animation = ""
        }, 300)
      } else {
        svg.setAttribute("fill", "none")
        svg.setAttribute("stroke", "currentColor")
        path.setAttribute("fill", "none")
      }
    })
  })

  // Save button functionality
  const saveButtons = document.querySelectorAll(".save-btn")
  saveButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const svg = this.querySelector("svg")
      const path = svg.querySelector("path")

      if (svg.getAttribute("fill") === "none") {
        svg.setAttribute("fill", "currentColor")
        path.setAttribute("fill", "currentColor")
      } else {
        svg.setAttribute("fill", "none")
        path.setAttribute("fill", "none")
      }
    })
  })

  // Follow button functionality
  const followButtons = document.querySelectorAll(".follow-btn")
  followButtons.forEach((button) => {
    button.addEventListener("click", function () {
      if (this.textContent === "Follow") {
        this.textContent = "Following"
        this.style.backgroundColor = "#262626"
        this.style.color = "#fff"
      } else {
        this.textContent = "Follow"
        this.style.backgroundColor = "#0095f6"
        this.style.color = "#fff"
      }
    })
  })

  // Search functionality
  const searchInputs = document.querySelectorAll(".search-input")
  searchInputs.forEach((input) => {
    input.addEventListener("input", function () {
      const query = this.value.trim()
      if (query.length > 0) {
        // Show search results (you can populate this with AJAX)
        console.log("Searching for:", query)
      }
    })
  })

  // Comment form submission
  const commentForms = document.querySelectorAll(".add-comment")
  commentForms.forEach((form) => {
    const input = form.querySelector("input")
    const button = form.querySelector("button")

    button.addEventListener("click", (e) => {
      e.preventDefault()
      if (input.value.trim()) {
        // Here you would send the comment to your Django backend
        console.log("Comment:", input.value)
        input.value = ""
      }
    })

    input.addEventListener("keypress", (e) => {
      if (e.key === "Enter") {
        button.click()
      }
    })
  })

  // Image upload functionality
  const imageInput = document.getElementById("imageInput")
  const uploadArea = document.getElementById("uploadArea")
  const imagePreview = document.getElementById("imagePreview")
  const previewImg = document.getElementById("previewImg")

  if (imageInput && uploadArea && imagePreview && previewImg) {
    imageInput.addEventListener("change", (e) => {
      const file = e.target.files[0]
      if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
          previewImg.src = e.target.result
          uploadArea.style.display = "none"
          imagePreview.style.display = "block"
        }
        reader.readAsDataURL(file)
      }
    })

    // Drag and drop functionality
    uploadArea.addEventListener("dragover", (e) => {
      e.preventDefault()
      uploadArea.style.backgroundColor = "#1a1a1a"
    })

    uploadArea.addEventListener("dragleave", () => {
      uploadArea.style.backgroundColor = ""
    })

    uploadArea.addEventListener("drop", (e) => {
      e.preventDefault()
      uploadArea.style.backgroundColor = ""
      const files = e.dataTransfer.files
      if (files.length > 0) {
        const file = files[0]
        if (file.type.startsWith("image/")) {
          const reader = new FileReader()
          reader.onload = (e) => {
            previewImg.src = e.target.result
            uploadArea.style.display = "none"
            imagePreview.style.display = "block"
          }
          reader.readAsDataURL(file)
        }
      }
    })
  }

  // Double tap to like (mobile)
  let lastTap = 0
  const postImages = document.querySelectorAll(".post-image")

  postImages.forEach((image) => {
    image.addEventListener("touchend", function (e) {
      const currentTime = new Date().getTime()
      const tapLength = currentTime - lastTap

      if (tapLength < 500 && tapLength > 0) {
        // Double tap detected
        const likeButton = this.closest(".post").querySelector(".like-btn")
        if (likeButton) {
          const svg = likeButton.querySelector("svg")
          if (svg.getAttribute("fill") === "none") {
            likeButton.click()

            // Show heart animation
            const heart = document.createElement("div")
            heart.innerHTML = "❤️"
            heart.style.cssText = `
              position: absolute;
              top: 50%;
              left: 50%;
              transform: translate(-50%, -50%) scale(0);
              font-size: 60px;
              pointer-events: none;
              z-index: 10;
              animation: heartPop 0.8s ease-out;
            `

            this.parentElement.style.position = "relative"
            this.parentElement.appendChild(heart)

            setTimeout(() => {
              heart.remove()
            }, 800)
          }
        }
      }
      lastTap = currentTime
    })
  })

  // Navigation active states
  const navItems = document.querySelectorAll(".nav-item")
  navItems.forEach((item) => {
    item.addEventListener("click", function () {
      navItems.forEach((nav) => nav.classList.remove("active"))
      this.classList.add("active")
    })
  })

  // Close search items
  const closeButtons = document.querySelectorAll(".close-btn")
  closeButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      e.stopPropagation()
      this.closest(".search-item").remove()
    })
  })
})

// CSS animations
const style = document.createElement("style")
style.textContent = `
  @keyframes heartPop {
    0% { transform: translate(-50%, -50%) scale(0); opacity: 0; }
    50% { transform: translate(-50%, -50%) scale(1.2); opacity: 1; }
    100% { transform: translate(-50%, -50%) scale(0); opacity: 0; }
  }

  .nav-item.active {
    font-weight: 700;
  }

  .nav-item.active .nav-icon {
    fill: currentColor;
  }
`
document.head.appendChild(style)

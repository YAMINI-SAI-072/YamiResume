function showAlert(level) {
  alert("Redirecting to your " + level + " certificate page.");
  window.location.href = level.toLowerCase() + ".html";
}

document.addEventListener('DOMContentLoaded', () => {
  function lookup() {
    fetch('/lookup?word='+document.getElementById("search").value)
      .then(res => res.json()
      .then(data => {
        document.getElementById("result").innerHTML = data;
      }));
  }

  const button = document.getElementById("go");
  button.addEventListener('click',lookup);
})

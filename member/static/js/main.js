window.onload = function(){
    setInterval(setWatch, 1000);

      function setWatch() {
        const date = new Date();
        let now = date.toLocaleTimeString();
        document.getElementById("demo").innerHTML = now;
      }
}
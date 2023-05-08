// 디지털 시계
window.onload = function(){
    setInterval(setWatch, 1000);

    function setWatch(){
        let date = new Date()
        let now = date.toLocaleTimeString();  // 시간 형식
        document.getElementById('demo').innerHTML = now
    }
}
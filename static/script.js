'use strict';
$(document).ready(function () {

  console.log("already!");

  setTimeout(function () {
    $("#movieCreatedSuccess").hide()
  }, 5000);

  setUrlAgain(window.location.href)

  function setUrlAgain(urlCurrent) {
    if (urlCurrent == "https://groovy-plating-222519.appspot.com/addMovie" || urlCurrent == "https://groovy-plating-222519.appspot.com/addImage") {
      urlCurrent = "https://groovy-plating-222519.appspot.com/"
      window.location.href = urlCurrent
    }
    if (urlCurrent == "http://localhost:8080/addMovie" || urlCurrent == "http://localhost:8080/addImage") {
      urlCurrent = "http://localhost:8080/"
      window.location.href = urlCurrent
    }
  }
});



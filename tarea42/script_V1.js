var es_chrome = navigator.userAgent.toLowerCase().indexOf('chrome') > -1;
if(es_chrome){
			    //alert("El navegador que se está utilizando es Chrome");
} else {
			    alert("El navegador que se está utilizando reconoce los comandos de voz");
}


var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent


var comandos = [ 'play' , 'stop'];
var grammar = '#JSGF V1.0; grammar comandos;'

var recognition = new SpeechRecognition();
var speechRecognitionList = new SpeechGrammarList();
speechRecognitionList.addFromString(grammar, 1);
recognition.grammars = speechRecognitionList;
recognition.continuous = false;
recognition.lang = 'en-US';
recognition.interimResults = false;
recognition.maxAlternatives = 1;

var diagnostic = document.querySelector('.output');
var bg = document.querySelector('html');
var hints = document.querySelector('.hints');
var qVideo = document.getElementById("qVideo");


hints.style.backgroundColor = "green";
hints.innerHTML = 'Haz click aquí y di "play" para reproducir el video y "stop" para detenerlo.';


hints.onclick = function() {
  hints.style.backgroundColor = "red";
  recognition.start();
}

recognition.onresult = function(event) {

  var orden = event.results[0][0].transcript;
  switch (orden){
	case 'play':
		diagnostic.textContent = 'Reproducimos: ' + orden + '.';
		hints.style.backgroundColor = "green";
		qVideo.play();
		break;
	case 'stop':
		diagnostic.textContent = 'Paramos: ' + orden + '.';
		hints.style.backgroundColor = "green";
		qVideo.pause();
		break;
	default:
		diagnostic.textContent = 'No es un comando: ' + orden + '.';
  }

}

recognition.onspeechend = function() {
  recognition.stop();
}

recognition.onnomatch = function(event) {
  diagnostic.textContent = "No he entendido la orden";
}

recognition.onerror = function(event) {
  diagnostic.textContent = 'Error: ' + event.error;
}

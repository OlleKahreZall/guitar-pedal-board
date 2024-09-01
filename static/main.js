let mediaRecorder;
let audioChunks = [];

document.getElementById('startButton').onclick = function() {
    navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
        const audioRecording = document.getElementById('audioRecording');
        audioRecording.srcObject = stream;
        audioRecording.controls = true;
        
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };
        mediaRecorder.start();
        
        document.getElementById('startButton').disabled = true;
        document.getElementById('stopButton').disabled = false;
    })
    .catch(error => {
        console.error('Error accessing microphone:', error);
    });
};

document.getElementById('stopButton').onclick = function() {
    mediaRecorder.stop();
    document.getElementById('startButton').disabled = false;
    document.getElementById('stopButton').disabled = true;
    
    const audioRecording = document.getElementById('audioRecording');
    const audioPlayback = document.getElementById('audioPlayback');
    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
    audioRecording.src = URL.createObjectURL(audioBlob);
    audioPlayback.src = URL.createObjectURL(audioBlob);
};


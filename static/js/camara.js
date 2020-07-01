/**
 * 
 */

window.onload = async () => {
	  const video = document.getElementById('monitor');
	  const foto1 = document.getElementById('foto1');
	  const foto2 = document.getElementById('foto2');
	  const foto3 = document.getElementById('foto3');
	  const shutter1 = document.getElementById('dispara1');
	  const shutter2 = document.getElementById('dispara2');
	  const shutter3 = document.getElementById('dispara3');
	  const stop = document.getElementById('stopCamara');
	 

	  try {
	    video.srcObject = await navigator.mediaDevices.getUserMedia({video: true});

	    await new Promise((resolve) => video.onloadedmetadata = resolve);
	    foto1.width,foto2.width ,foto3.width  = 240;
	    foto1.height,foto2.height,foto3.height = 180;
	    //alert(video.videoWidth);
	    stop.onclick=()=>video.stop();
	    shutter1.onclick = () =>foto1.getContext('2d').drawImage(video,0,0,240 ,180);
	    shutter2.onclick = () =>foto2.getContext('2d').drawImage(video,0,0,240 ,180);
	    shutter3.onclick = () =>foto3.getContext('2d').drawImage(video,0,0,240 ,180);
	    
	  } catch (err) {
	    console.error(err);
	  }
	};

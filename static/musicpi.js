function makeControlRequest(value) {
    var httpRequest;
  console.log("makeControlRequest");
    if (window.XMLHttpRequest) { // Mozilla, Safari, ...
        httpRequest = new XMLHttpRequest();
    }

    if (!httpRequest) {
        alert('中断 :( XMLHTTP インスタンスを生成できませんでした');
        return false;
    }

    httpRequest.onreadystatechange = function() { alertContents(httpRequest); };
    request = '/' + value;
    httpRequest.open('GET', request, true);
    httpRequest.send('');
}

function alertContents(httpRequest) {
    if (httpRequest.readyState == 4) {
        if (httpRequest.status == 200) {
          console.log(httpRequest.responseText);
        } else {
            console.log('リクエストに問題が発生しました');
        }
    }
}
% include('header.tpl', title='{{title}}')

<nav class="navbar navbar-default navbar-static-top">  
    <p class="navbar-text"><a class="navbar-link" href="/power">Power</a></p>
    <p class="navbar-text"><a class="navbar-link" href="/qr">QR Code</a></p>
</nav>

<div class="btn-group">
  <button type="button" class="btn btn-default"   onclick="makeControlRequest('stop')">
    <span class="glyphicon glyphicon-stop"></span>
    <span id="stop">Stop</span>
  </button>
  <button type="button" class="btn btn-default" onclick="makeControlRequest('volume/increase')">
    <span class="glyphicon glyphicon-volume-up"></span>
    <span id="up">Volume Up</span>
  </button>

  <button type="button" class="btn btn-default" onclick="makeControlRequest('volume/decrease')">
    <span class="glyphicon glyphicon-volume-down"></span>
    <span id="down">Volume Down</span>
  </button>
</div>


%if channels:
    <div class="channel_list row">
     %for channel in channels:
      <div class="btn btn-default col-md-2"
           onclick="makeControlRequest('{{channel}}')">{{channel}}</div>
    %end
    </div>	
%else:
    <h1>Channel is NOT available!</h1>
%end

<div>
  <p id="streamtitle"></p>
</div>

% include('footer.tpl')

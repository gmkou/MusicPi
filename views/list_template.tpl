% include('header.tpl', title='{{title}}')

<div class="navbar">
  <div id="power"><a href="/power">Power</a></div>
  <div id="qr"><a href="/qr">QR Code</a></div>
</div>

<div class="control">
<span id="stop" class="btn btn-default"><a href="/stop">Stop</a></span>
<span id="up"  class="btn btn-default"><a href="/up">Volume Up</a></span>
<span id="down"  class="btn btn-default"><a href="/down">Volume Down</a></span>
</div>


%if channels:
    <div class="channel_list row">
     %for channel in channels:
      <div class="btn btn-default col-md-2"><a href="/{{channel}}">{{channel}}</a></div>
    %end
    </div>	
%else:
    <h1>Channel is NOT available!</h1>
%end

% include('footer.tpl')
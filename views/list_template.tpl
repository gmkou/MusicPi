% include('header.tpl', title='{{title}}')

<div class="special_control">
<div id="power"><a href="/power">Power</a></div>
<div id="qr"><a href="/qr">QR Code</a></div>
</div>

<div class="control">
<span id="stop"><a href="/stop">Stop</a></span>
<span id="up"><a href="/up">Volume Up</a></span>
<span id="down"><a href="/down">Volume Down</a></span>
</div>

%if channels:
    <div class="channel_list">
     %for channel in channels:
      <div class="channel"><a href="/{{channel}}">{{channel}}</a></div>
    %end
    </div>	
%else:
    <h1>Channel is NOT available!</h1>
%end

% include('footer.tpl')
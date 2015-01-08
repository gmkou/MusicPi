% include('header.tpl', title='{{title}}')

<div class="control">
<span id="power"><a href="/power">Power</a></span>
<span id="stop"><a href="/stop">Stop</a></span>
<span id="up"><a href="/up">Volume Up</a></span>
<span id="down"><a href="/down">Volume Down</a></span>
<span id="qr"><a href="/qr">QR Code</a></span>
</div>

%if channels:
    <div class="channel_list row">
     %for channel in channels:
      <span class="channel .col-xs-6 .col-sm-1"><a href="/{{channel}}">{{channel}}</a></span>
    %end
    </div>	
%else:
    <h1>Channel is NOT available!</h1>
%end

% include('footer.tpl')
<ul class="control">
<li id="power"><a href="/power">Power</a></li>
<li id="stop"><a href="/stop">Stop</a></li>
<li id="up"><a href="/up">Volume Up</a></li>
<li id="down"><a href="/down">Volume Down</a></li>
<li id="qr"><a href="/qr">QR Code</a></li>
</ul>

%if channels:
    <ul>
     %for channel in channels:
      <li class="channel"><a href="/{{channel}}">{{channel}}</li>
    %end
    </ul>	
%else:
    <h1>List is NOT available!</h1>
%end
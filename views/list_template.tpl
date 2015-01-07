%if channels:
    <h1>Radio is available!</h1>
    %for channel in channels:
      <li>{{channel}}</li>
    %end
%else:
    <h1>List is NOT available!</h1>
%end
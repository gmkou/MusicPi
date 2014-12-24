%if files:
    <h1>List is available!</h1>
    %for file in files:
      <li>{{file}}</li>
    %end
%else:
    <h1>List is NOT available!</h1>
%end
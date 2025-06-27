---
title: Team
nav:
  order: 4
  tooltip: Meet the team
---

{% include section.html %}

# Quick Links

{%
  include button.html
  icon="fa-solid fa-people-group"
  text="Alumni"
  link="/team/alumni"
%}
{%
  include button.html
  icon="fa-solid fa-people-group"
  text="Collaborators"
  link="/collaborators"
%}
{%
  include button.html
  icon="fa-solid fa-door-open"
  text="Join us"
  link="/team/join"
%}



Our lab is made up of a talented mix of graduate students, postdoctoral researchers, programmers, and staff, and their backgrounds range from pure computer science to experimental biology. If you're interested in joining this diverse and dynamic team, please reach out!

{% include section.html %}

{% include list.html data="members" component="portrait" filters="group: active, role: pi" %}


{% include section.html %}

# {% include icon.html icon="fa-solid fa-users" %}Researchers

{% include list.html data="members" component="portrait" filters="group: active, role: senior" %}

<br>

{% include list.html data="members" component="portrait" filters="group: active, role: phd" %}
<br>

{% include list.html data="members" component="portrait" filters="group: active, role: combined" %}

<br>
{% include list.html data="members" component="portrait" filters="group: active, role: master" %}

# {% include icon.html icon="fa-solid fa-users" %}Interns

{% include list.html data="members" component="portrait" filters="group: active, role: intern" %}

{% include section.html %}

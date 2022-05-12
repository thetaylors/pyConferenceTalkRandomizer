

let get_random_boolean = () => Math.floor(Math.random() * 2) == 1 ? true : false;

let get_random_url = () => talks[Math.floor(Math.random() * talks.length)];

let get_random_url_only_latest = () => {
    date_of_latest = date_of_latest_talk();
    return talks[Math.floor(Math.random() * no_of_talks_in_latest_conf(date_of_latest.year, date_of_latest.month))];
}

let set_talk_link = (show_badge=false) => {
    if (document.getElementById('prioritize_latest').checked || get_random_boolean()) {
        talk_url = get_random_url_only_latest();
    } else {
        talk_url = get_random_url();
    }
    document.getElementById("talk_link").href = talk_url;
    console.log(talk_url);

    if (show_badge) {
        badge_elem = document.getElementById('badge');
        if (badge_elem.className == 'badge bg-info') {
            badge_class_val = 'badge bg-primary';
        } else {
            badge_class_val = 'badge bg-info';
        }

        badge_elem.innerText = 'Updated link';
        badge_elem.className = badge_class_val;
    }
}

let check_or_uncheck = () => {
  // TODO if the url param exists, set accordingly
};

let date_of_latest_talk = () => {
    split_url = talks[0].split('/');
    if (split_url.length > 1) {
      year = split_url[split_url.length - 3];
      month = split_url[split_url.length - 2];
      return { 'year': year, 'month': month }
    } else {
      console.log('Unable to split the latest talk url.');
    }
}

let no_of_talks_in_latest_conf = (year, month) => {
    let talk_step = 0;
    // the max step is currently 60 as there haven't been more than 51 talks in a conference, so far
    for (let step = 1; step < 60; step++) {
        if (talks[step].includes(year) && talks[step].includes(month)) {
          continue;
        }
          talk_step = step;
          break;
        }
        return talk_step;
}

let save_checkbox_state = () => {
    checkbox = document.getElementById('prioritize_latest');
    window = document.defaultView;
    window.localStorage.setItem('checkbox_state', checkbox.checked);
}

let read_checkbox_state = () => {
    window = document.defaultView;
    return (window.localStorage.getItem('checkbox_state') === 'true');
}

let set_checkbox_state = () => {
    checkbox = document.getElementById('prioritize_latest');
    new_state = read_checkbox_state();
    console.log('new state: ' + new_state)
    checkbox.checked = new_state;
}
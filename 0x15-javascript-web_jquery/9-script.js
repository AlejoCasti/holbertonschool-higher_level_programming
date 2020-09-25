$(document).ready($.get('https://fourtonfish.com/hellosalut/?lang=fr', ({hello}) => {
      $('#hello').text(hello)
}))
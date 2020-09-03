$('.field-email').change(function(){
    current_val = $(this).val();
    $pattern='/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/'
    if (eregi($pattern, $current_val)){
        return true;
     }
     else {
        window.alert("You have entered an invalid email address!")
        return false;
    }
$('.contact_no').change(function(){
    current_val = $(this).val();
     if (eregi(current_val.length != 10)){
        return true;
     }
     else {
        window.alert("Phone number must be 10 digits.")
        return false;
    }
$('.field-password').change(function(){
    pwd = $(this).val();
    $pattern='(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}'
    if (eregi($pattern, pwd)){
        return true;
     }
     else {
        window.alert("You have entered an invalid password!")
        return false;
    }
 $('.field-confirm_password').change(function(){
    current_val = $(this).val();
    if (eregi($pwd=$current_val)){
        return true;
     }
     else {
        window.alert("Passwords do no match!")
        return false;
    }

  $('.field-rfid_no').change(function(){
    current_val = $(this).val();
    $pattern='\\d{8,10}'
    if (eregi($pattern, $current_val)){
        return true;
     }
     else {
        window.alert("You have entered an invalid RFID number")
        return false;
    }
$('.field-vehicle_no').change(function(){
    current_val = $(this).val();
    $pattern = "^[a-zA-z]{2}\s[0-9]{2}\s[0-9]{4}$";
    if (eregi($pattern, $current_val)){
        return true;
     }
     else {
        window.alert("You have entered an invalid Vehicle nuumber!")
        return false;
    }

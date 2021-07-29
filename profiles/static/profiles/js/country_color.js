  
/* js for setting the colour of the Countryfield.
   All code taken from Code Institute's Boutique Ado
    project written by ckz8780.*/

    let countrySelected = $('#id_primary_country').val();
    if(!countrySelected) {
        $('#id_primary_country').css('color', '#507294');
    };
    $('#id_primary_country').change(function() {
        countrySelected = $(this).val();
        if(!countrySelected) {
            $(this).css('color', '#507294');
        } else {
            $(this).css('color', '#000');
        }
    });
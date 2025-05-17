function filter_materials() {
        checkboxes = $("input.material_checkbox")
        checkboxes.each(function(index) {
                console.log(index + ": " + $(this));
        });

        console.log(checkboxes)
}

$(document).ready(function(){
        filter_materials()
});

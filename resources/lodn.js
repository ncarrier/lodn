function filter_materials() {
        materials = []
        checkboxes = $("input.material_checkbox")
        checkboxes.each(function(index) {
                if ($(this).attr("checked")) {
                        materials.push($(this).attr("id"))
                }
        });
        console.log(materials);

        origamis = $("div.origami")
        origamis.each(function(){
                $(this).hide();
                classes = $(this).attr("class").split(" ")
                console.log(classes)
                classes.forEach((c) => {
                        if (materials.includes(c)) {
                                $(this).show()
                        }
                })
        })
}

$(document).ready(function(){
        filter_materials()
});

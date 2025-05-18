/**
 * Hides / shows the origamis depending on if a material they can be folded
 * with, is enabled in the filtering section.
 */
function filter_materials() {
        // create the list of checked materials
        materials = []
        checkboxes = $("input.material_checkbox")
        checkboxes.each(function(index) {
                if (checkboxes[index].checked) {
                        materials.push($(this).attr("id"))
                }
        });

        // hide all origamis then re-show those matching the categories enabled
        $("div.origami").each(function(){
                $(this).hide();
                classes = $(this).attr("class").split(" ")
                classes.forEach((c) => {
                        if (materials.includes(c)) {
                                $(this).show()
                        }
                })
        })
}

/**
 * Compute the dimensions of the origamis based on their original dimensions,
 * their original paper sizes and the requested paper size.
 */
function compute_sizes() {
        description_cells = $("td.description")
        current_size = $("#size").val()

        description_cells.each(function(){
                diameter_text = $(this).find(".diameter_text")
                if (diameter_text.length == 0)
                        return;
                paper_size = $(this).find(".paper_size").attr("value")
                if (paper_size == 0) {
                        diameter_text.text("Pas de taille de papier définie dans le catalogue")
                        return;
                }
                base_diameter = $(this).find(".diameter").attr("value")
                /* sizes are in mm in the catalog, but in cm in the web page */
                new_diameter = (base_diameter * current_size * 10) / paper_size;
                diameter_text.text("diamètre: " + (new_diameter / 10) + " cm")
        });

}

$(document).ready(function(){
        filter_materials()
        $("input.material_checkbox").each(function() {
                $(this).click(function() {
                        filter_materials();
                })
        })
        compute_sizes()
        $(document).on('input', '#size', function(){
                compute_sizes();
        })
});

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
        console.log(current_size)
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

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
                paper_size = $(this).find(".paper_size").attr("value")
                dimensions = ["diameter", "height", "length", "width"]
                dimensions.forEach((d) => {
                        text = $(this).find("." + d + "_text")
                        if (text.length == 0)
                                return;
                        if (paper_size == 0) {
                                text.text("Pas de taille de papier définie dans le catalogue")
                                return;
                        }
                        base_dimension = $(this).find("." + d).attr("value")
                        /* sizes are in mm in the catalog, but in cm in the web page */
                        new_dimension = (base_dimension * current_size * 10) / paper_size;
                        text.text(d + ": " + (Math.round(new_dimension) / 10) + " cm")
                })
        });
}

function update_mailto() {

}

function update_prequote() {
        prequote = $("#prequote");
        text = `<table>
  <tr>
    <th>Nom</th>
    <th>Quantité</th>
    <th>Durée unitaire</th>
    <th>Durée totale</th>
  </tr>`;
        hourly_rate = $("#hourly_rate").val()
        console.log(hourly_rate);
        total_duration = 0;
        $("div.origami").each(function() {
                quotation = $(this).find(".quotation").attr("value");
                if (quotation == 0)
                        return;
                origami_num = $(this).find(".origami_num").val()
                if (origami_num == 0)
                        return;
                origami_name = $(this).find(".origami_name").attr("value");
                console.log(origami_name);
                unit_duration = quotation / 10;
                duration = unit_duration * origami_num;
                text += `  <tr>
    <td>${origami_name}</td>
    <td>${origami_num}</td>
    <td>${unit_duration}</td>
    <td>${duration}</td>
  </tr>`;
                total_duration += duration;
        });
        ti_price = Math.round((total_duration * hourly_rate) / 60);
        wt_price = Math.round(100 * (ti_price / 1.20)) / 100;
        text += `</table>
<p>durée totale : ${total_duration}</p>
<p>prix TTC : ${ti_price}</p>
<p>prix HT : ${wt_price}</p>
        `
        prequote.html(text);

        update_mailto();
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
        update_prequote();
        $("input.origami_num").each(function() {
                $(this).click(function() {
                        update_prequote();
                })
        })
});

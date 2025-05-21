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

dimension_translation = {
        "diameter": "diamètre",
        "height": "hauteur",
        "length": "longeur",
        "width": "largeur"
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
                        text.text(`${dimension_translation[d]} : ${(Math.round(new_dimension) / 10)} cm`)
                })
        });
}

function format_duration_in_minutes(duration) {
        hours = Math.floor(duration / 60);
        minutes = Math.round(duration) % 60;

        if (hours != 0)
                return `${hours} h ${minutes} min`;

        return `${minutes} min`;
}

/**
 * Generates a prequote and insert it in html, in the page and in csv form in
 * the mailto link.
 */
function update_prequote_and_mailto() {
        prequote = $("#prequote");
        mailto_link = $("#prequote_mail");

        // headers
        prequote_text = `<table>
  <tr>
    <th>Nom</th>
    <th>Quantité</th>
    <th>Durée unitaire (min)</th>
    <th>Durée totale (min)</th>
  </tr>`;
        mailto_text = `


Ne pas modifier le texte sous la ligne suivante.
---------------------------------------------------------------
Nom;Quantité;Durée unitaire;Durée totale
`

        // bodies
        hourly_rate = $("#hourly_rate").val()
        total_duration = 0;
        $("div.origami").each(function() {
                quotation = $(this).find(".quotation").attr("value");
                if (quotation == 0)
                        return;
                origami_num = $(this).find(".origami_num").val()
                if (origami_num == 0)
                        return;
                origami_name = $(this).find(".origami_name").attr("value");
                unit_duration = quotation / 10;
                duration = unit_duration * origami_num;
                prequote_text += `  <tr>
    <td>${origami_name}</td>
    <td>${origami_num}</td>
    <td>${unit_duration}</td>
    <td>${format_duration_in_minutes(duration)}</td>
  </tr>`;
                mailto_text += `${origami_name};${origami_num};${unit_duration};${duration}
`
                total_duration += duration;
        });

        // footers
        ti_price = Math.round((total_duration * hourly_rate) / 60);
        wt_price = Math.round(100 * (ti_price / 1.20)) / 100;
        prequote_text += `</table>
<p>Durée totale : ${format_duration_in_minutes(total_duration)}<br/>
Prix TTC : ${ti_price} €<br/>
Prix HT : ${wt_price} €</p>
`
        mailto_text += `
---------------------------------------------------------------
Durée totale : ${format_duration_in_minutes(total_duration)}
Prix TTC : ${ti_price} €
Prix HT : ${wt_price} €
`

        // application
        prequote.html(prequote_text);

        subject = encodeURIComponent("Demande de devis")
        body = encodeURIComponent(mailto_text)
        link = `mailto:carriern@outlook.fr?subject=${subject}&body=${body}`;
        mailto_link.attr("href", link)
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
        update_prequote_and_mailto();
        $("input.origami_num").each(function() {
                $(this).on('input', function() {
                        update_prequote_and_mailto();
                });
        })
});

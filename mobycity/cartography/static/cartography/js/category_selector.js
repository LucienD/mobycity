//********** CATEGORY SELECTOR **********
var categoryCheckboxButtons = document.getElementsByName("cartography_category");

// Parcourt les checkbox des categories
for (var i = 0, n = categoryCheckboxButtons.length; i < n; i++) {
    //********** Action au clic sur une checkbox **********
    categoryCheckboxButtons[i].onclick = function() {
        // Affiche ou cache les marqueurs
        displayOrHideMarkers(cartographyMarkers[0], this.value, this.checked);

        // Coche la checkbox 'all' si toutes les checkbox sont cochees, sinon la decoche
        var allChecked = true;

        for (var i = 0, n = categoryCheckboxButtons.length; i < n; i++) {
            if (!categoryCheckboxButtons[i].checked) {
                allChecked = false;
            }
        }

        if (allChecked) {
            document.getElementById("id_cartography_category_all").checked = true;
        } else {
            document.getElementById("id_cartography_category_all").checked = false;
        }
    };
}

//********** Action au clic sur la checkbox 'all' **********
document.getElementById("id_cartography_category_all").onclick = function() {
    // Parcourt les checkbox des categories
    for (var i = 0, n = categoryCheckboxButtons.length; i < n; i++) {
        // Coche ou decoche toutes les checkbox
        categoryCheckboxButtons[i].checked = this.checked;
        // Affiche ou cache les marqueurs
        displayOrHideMarkers(cartographyMarkers[0], categoryCheckboxButtons[i].value, this.checked);
    }
};
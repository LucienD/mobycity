var mapCenter = new google.maps.LatLng(centerLat, centerLng);

var mapOptions = {
        scrollwheel : false,
        styles: mapStyles,
        center: { lat: mapCenter.lat(), lng: mapCenter.lng() },
        zoom: 12
    };

// Liste des cartes de la page
var cartographyMaps = [];

for (var i = 0; i < document.getElementsByClassName('cartography-map').length; i++) {
    cartographyMaps[i] = new google.maps.Map(document.getElementsByClassName('cartography-map')[i], mapOptions);
}

var cartographyMarkers = [];

// Initialisation des cartes listees
function mapsInitialize() {
    for (var i = 0, a = cartographyMaps.length; i < a; i++) {
        map = cartographyMaps[i];
        cartographyMarkers[i] = [];

        // Positionnement des points d'interet
        for (var j = 0, b = pointOfInterestList.length; j < b; j++) {
            var poi = pointOfInterestList[j].fields;
            var geolocation = poi.geolocation.split(',');
            var icon, image;

            // Attribution des images et icones en fonction de la categorie
            for (var k = 0, c = categoryList.length; k < c; k++) {
                if (categoryList[k].pk == poi.category) {
                    icon = mediaBaseUrl + categoryList[k].fields.image;
                    
                    if (!poi.image) { // Pas d'image donc placeholder
                        image = mediaBaseUrl + categoryList[k].fields.placeholder_image;
                    } else {
                        image = mediaBaseUrl + poi.image;
                    }
                }
            }

            // Positionnement du marqueur
            var marker = new google.maps.Marker({
                map: map,
                position: {
                    lat: parseFloat(geolocation[0]),
                    lng: parseFloat(geolocation[1])
                },
                title: poi.name,
                icon: icon
            });

            marker.id = pointOfInterestList[j].pk;
            marker.category = poi.category;

            // Infobulle du marqueur
            var contentString = '<div class="cartography-poi-infobox">'
                                    + '<div class="cartography-poi-infobox-image">'
                                        + '<img src="' + image + '" />'
                                    + '</div>'
                                    + '<div class="cartography-poi-infobox-text">'
                                        + '<h1>' + marker.title + '</h1>'
                                        + '<div class="cartography-poi-infobox-address">' + poi.address + '</div>'
                                        + '<div class="cartography-poi-infobox-description">';
            
            if (poi.phone) {
                contentString += '<p class="test">Téléphone : ' + poi.phone + '</p>';
            }
            
            if (poi.website) {
                contentString += '<p>Site web : <a href="' + poi.website + '">' + poi.website + '</a></p>';
            }
            
            if (poi.opening_hours) {
                contentString += '<p>Horaires : ' + poi.opening_hours + '</p>';
            }
            
            contentString += poi.description
                                        + '</div>' // .cartography-poi-infobox-text
                                    + '</div>' // .cartography-poi-infobox
                                    + '<img class="cartography-poi-infobox-icon" onclick="hideInfoBox(' + i + ', ' + marker.id + ')" src="' + marker.icon + '" />'
                                + '</div>';
            
            var infoBoxContent = document.createElement('div');
            infoBoxContent.style.cssText = 'height: 100%; width: 100%;';
            infoBoxContent.innerHTML = contentString;

            var infoBoxOptions = {
                boxStyle: { 
                    background: '#fff',
                    border: 'solid 1px #ddd',
                    opacity: 1,
                    height: '400px',
                    width: '250px'
                },
                closeBoxMargin: '10px 2px 2px 2px',
                closeBoxURL: '',
                content: infoBoxContent,
                disableAutoPan: false,
                enableEventPropagation: false,
                infoBoxClearance: new google.maps.Size(1, 1),
                isHidden: true,
                maxWidth: 0,
                pane: 'floatPane',
                pixelOffset: new google.maps.Size(-125, -416)
            };

            marker.infoBox = new InfoBox(infoBoxOptions);
            marker.infoBox.open(map, marker);
            
            var markers = cartographyMarkers[i];
            
            marker.addListener('click', function () {
                if (this.infoBox.isHidden_) {
                    for (var k = 0, c = markers.length; k < c; k++) {
                        marker = markers[k].infoBox.hide();
                    }
                    
                    this.infoBox.show();
                } else {
                    this.infoBox.hide();
                }
            });
            
            cartographyMarkers[i].push(marker);
        }

        // Recentrage de la carte en cas de sortie des limites
        google.maps.event.addListener(map, 'dragend', function() {
            if (map.initialBounds) {
                if (map.initialBounds.contains(map.getCenter())) return;

                // We're out of bounds - Move the map back within the bounds

                var c = map.getCenter(),
                    x = c.lng(),
                    y = c.lat(),
                    maxX = map.initialBounds.getNorthEast().lng(),
                    maxY = map.initialBounds.getNorthEast().lat(),
                    minX = map.initialBounds.getSouthWest().lng(),
                    minY = map.initialBounds.getSouthWest().lat();

                if (x < minX) x = minX;
                if (x > maxX) x = maxX;
                if (y < minY) y = minY;
                if (y > maxY) y = maxY;

                map.setCenter(new google.maps.LatLng(y, x));
            }
        });
    }

    // Initialisation des limites de la carte
    google.maps.event.addListener(map, 'bounds_changed', function() {
        if (!map.initialBounds) {
            map.initialBounds = map.getBounds();
        }
    });
}

// Cache une infobulle
function hideInfoBox(mapId, markerId) {
    var marker;
    
    for (var i = 0, a = cartographyMarkers[mapId].length; i < a; i++) {
        marker = cartographyMarkers[mapId][i];
        
        if (marker.id == markerId) {
            marker.infoBox.hide();
        }
    }
}

function displayOrHideMarkers(markers, category, display) {
    for (var i = 0, n = markers.length; i < n; i++) {
        if (markers[i].category == category) {
            if (display) {
                markers[i].setVisible(true);
            } else {
                markers[i].setVisible(false);
            }
        }
    }
}

google.maps.event.addDomListener(window, 'load', mapsInitialize);

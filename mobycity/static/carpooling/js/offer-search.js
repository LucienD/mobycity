function markerPositionChanged(event) {
    document.getElementById(this.latitudeInputId).value = event.latLng.lat();
    document.getElementById(this.longitudeInputId).value = event.latLng.lng();
}
    
//********** Point A **********
latA = mapCenter.lat() - 0.002 * 2;
lngA = mapCenter.lng() - 0.003 * 2;

if (document.getElementById('id_departure_latitude').value && document.getElementById('id_departure_longitude').value) {
    latA = parseFloat(document.getElementById('id_departure_latitude').value);
    lngA = parseFloat(document.getElementById('id_departure_longitude').value);
}

var markerImageA = new google.maps.MarkerImage(
    markerIconA,
    new google.maps.Size(17, 17),
    new google.maps.Point(0, 0),
    new google.maps.Point(8, 8)
);

var carpoolMarkerA = new google.maps.Marker({
    position : {
        lat : latA,
        lng : lngA
    },
    map : cartographyMaps[0],
    draggable : true,
    label : markerLabelA,
    icon: markerImageA
});
carpoolMarkerA.latitudeInputId = 'id_departure_latitude';
carpoolMarkerA.longitudeInputId = 'id_departure_longitude';
document.getElementById(carpoolMarkerA.latitudeInputId).value = carpoolMarkerA.position.lat();
document.getElementById(carpoolMarkerA.longitudeInputId).value = carpoolMarkerA.position.lng();
google.maps.event.addListener(carpoolMarkerA, 'dragend', markerPositionChanged);

//********** Point B **********
latB = mapCenter.lat() + 0.002 * 2;
lngB = mapCenter.lng() + 0.003 * 2;

if (document.getElementById('id_arrival_latitude').value && document.getElementById('id_arrival_longitude').value) {
    latB = parseFloat(document.getElementById('id_arrival_latitude').value);
    lngB = parseFloat(document.getElementById('id_arrival_longitude').value);
}

var markerImageB = new google.maps.MarkerImage(
    markerIconB,
    new google.maps.Size(17, 17),
    new google.maps.Point(0, 0),
    new google.maps.Point(8, 8)
);

var carpoolMarkerB = new google.maps.Marker({
    position : {
        lat : latB,
        lng : lngB
    },
    map : cartographyMaps[0],
    draggable : true,
    label : markerLabelB,
    icon: markerImageB
});
carpoolMarkerB.latitudeInputId = 'id_arrival_latitude';
carpoolMarkerB.longitudeInputId = 'id_arrival_longitude';
document.getElementById(carpoolMarkerB.latitudeInputId).value = carpoolMarkerB.position.lat();
document.getElementById(carpoolMarkerB.longitudeInputId).value = carpoolMarkerB.position.lng();
google.maps.event.addListener(carpoolMarkerB, 'dragend', markerPositionChanged);

//********** Affichage **********
function displayOccOrReg() {
    var frequencyWidget = document.getElementsByName('frequency');
    
    for (i = 0, a = frequencyWidget.length; i < a; i++) {
        if (frequencyWidget[i].value == 'OCC' && frequencyWidget[i].checked) {
            document.getElementById('occ').style.display = 'block';
            document.getElementById('reg').style.display = 'none';
        } else if (frequencyWidget[i].value == 'REG' && frequencyWidget[i].checked) {
            document.getElementById('occ').style.display = 'none';
            document.getElementById('reg').style.display = 'block';
        }
    }
}

displayOccOrReg();

var frequencyWidget = document.getElementsByName('frequency');

for (i = 0, a = frequencyWidget.length; i < a; i++) {
    frequencyWidget[i].addEventListener('click', function() {
        displayOccOrReg();
    });
}

document.getElementById('id_occ_arrival_datetime_1').addEventListener('change', function() {
    document.getElementById('id_reg_arrival_time').value = document.getElementById('id_occ_arrival_datetime_1').value;
});

document.getElementById('id_reg_arrival_time').addEventListener('change', function() {
    document.getElementById('id_occ_arrival_datetime_1').value = document.getElementById('id_reg_arrival_time').value;
});
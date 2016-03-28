var map;
var infowindow;


function initMap() {
    var Logan = {lat: 41.926576, lng: -111.756374};
    
    map = new google.maps.Map(document.getElementById('map'), {
                              center: Logan,
                              zoom: 9
                              });
    
    infowindow = new google.maps.InfoWindow();
    
    var service = new google.maps.places.PlacesService(map);
    service.nearbySearch({
                         location: Logan,
                         radius: 100
                         }, callback);
}

function callback(results, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
        }
    }
}

function createMarker(place) {
    var placeLoc = place.geometry.location;
    var marker = new google.maps.Marker({
                                        map: map,
                                        position: place.geometry.location
                                        });
    
    google.maps.event.addListener(marker, 'click', function() {
                                  infowindow.setContent(place.name);
                                  infowindow.open(map, this);
                                  });
}

//var main = function() {
//    $(".travel-details").toggle();
//    $(".travel-button").click(function() {
//                            $(".travel-details").slideToggle();
//                            });
//};

$(document).ready(main);

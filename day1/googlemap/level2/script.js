let map;
let marker;
const statusDiv = document.getElementById('location-info');

function initMap() {

    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 37.5665, lng: 126.9780 }, // 서울 시청
        zoom: 8
    });

    marker = new google.maps.Marker({
        position: defaultLocation,
        map: map,
        title: '현재 위치'
    });
}

function getCurrentLocation() {}
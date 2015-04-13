angular.module('carpool').controller("ShowTripsController", function($location, $http, $scope, TripsData) {

    $http.get('/trips').success(function(tripsData){

        TripsData.getTrips().then(function (data) {
            $scope.trips = data.trips;
        });
    })
});
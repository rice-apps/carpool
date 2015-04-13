angular.module('carpool').controller("ShowTripsController", function($location, $http, $scope, TripsData) {

    TripsData.getTrips().then(function (data) {
        $scope.trips = data.trips;
    });
});
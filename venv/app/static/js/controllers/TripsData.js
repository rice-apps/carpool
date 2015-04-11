angular.module('carpool').factory('TripsData', function ($http, $q) {

  return {
    getTrips: function () {
      var deferred = $q.defer();
      $http.get('/trips').success(function (data) {
        deferred.resolve(data);
      });
      return deferred.promise;
    }
  };

});
angular.module('carpool', ['ngRoute'])

.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {

	    $routeProvider

      .when('/', {
        templateUrl: 'static/templates/test.html',
        controller: 'mainController'
      })
      .when('/newtrip', {
        templateUrl: 'static/templates/newtrip.html',
        controller: 'NewTripController'
      })
      .when('/trips', {
        templateUrl: 'static/templates/trips.html',
        controller: 'ShowTripsController'
      })
      .otherwise({
        redirectTo: '/'
      });

      // use the HTML5 History API
       //$locationProvider.html5Mode(true);

  }])

.controller('mainController', function($scope) {

    $scope.message = 'This is it!';

})
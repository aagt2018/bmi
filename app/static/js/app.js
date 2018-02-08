'use strict';

var bmiApp = angular.module('bmiApp', ['ngRoute',]);

bmiApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '/static/partials/index.html',
             }).
             when('/error', {
                 templateUrl: '../static/partials/error.html',
             }).
             when('/calculate', {
                 templateUrl: '../static/partials/calculate.html',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);


bmiApp.controller("bmiController", function($scope, $location, $http) {
    $scope.showResult = false;
    $scope.register = function() {
        var username = $scope.username;
        var password = $scope.password

        $http({
            method : "POST",
            url : "/register",
            data: {"username": username, "password": password}
        }).then(function mySuccess(response) {
                if (!response.data.was_added){
                    $location.path("error");
                }
                else {
                    $location.path("calculate");
                }
        }, function myError(response) {
        });
    };
    $scope.bmi = function() {
        var weight = $scope.weight;
        var height = $scope.height

        $http({
            method : "POST",
            url : "/bmi",
            data: {"weight": weight, "height": height}
        }).then(function mySuccess(response) {
            $scope.bmiResult = response.data.bmi;
            $scope.category = response.data.category;
            $scope.showResult = true;
        }, function myError(response) {
        });
    };
});
var app = angular.module('Home',[]);

app.controller('HomeController', function($scope, $window, $http, $sce) {
    $scope.tabTitle = $sce.trustAsHtml("Resum\u00E9");
    $scope.homeShow = true;
    $scope.projectsShow = false;

    $scope.gotoHome = function(){
        $scope.homeShow = true;
        $scope.projectsShow = false;
    };

    $scope.gotoProjects = function(){
        $scope.homeShow = false;
        $scope.projectsShow = true;
    }
});
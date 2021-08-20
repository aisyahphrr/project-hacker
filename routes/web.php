<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('index');
});

Route::get('/index.html', function () {
    return view('index');
});

Route::get('/chart.html', function () {
    return view('chart');
});

Route::get('/table.html', function () {
    return view('table');
});

Route::get('/form.html', function () {
    return view('form');
});

Route::get('/calendar.html', function () {
    return view('calendar');
});

Route::get('/map.html', function () {
    return view('map');
});

Route::get('/login.html', function () {
    return view('login');
});

Route::get('/button.html', function () {
    return view('index');
});
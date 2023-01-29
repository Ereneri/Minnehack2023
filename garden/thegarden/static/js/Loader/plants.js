import {GLTFLoader} from "./GLTFLoader.js";
import { OrbitControls } from "./OrbitControls.js";

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1,3000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );
var controls = new OrbitControls( camera, renderer.domElement );

var loader = new GLTFLoader();

var obj;
loader.load("./monstera_tree/scene.gltf", function (gltf){
    obj = gltf.scene;
    scene.add(gltf.scene);
    });
loader.load("./monstera_tree/scene.gltf", function (gltf){
    obj = gltf.scene;
    scene.add(gltf.scene);
    });
scene.background = new THREE.Color ("white");
var light = new THREE.HemisphereLight("white", "white", 2);
scene.add(light);
camera.position.set(0,10,100);

            

function animate(){
    requestAnimationFrame( animate );
    controls.update();
    renderer.render(scene, camera);
    }
animate();
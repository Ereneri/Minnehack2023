import {GLTFLoader} from "./GLTFLoader.js";
import { OrbitControls } from "./OrbitControls.js";
import { SphericalHarmonics3 } from "./three.module.js";

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1,2000);
var renderer = new THREE.WebGLRenderer();

renderer.setSize( window.innerWidth, (window.innerHeight/2 ));
document.body.appendChild( renderer.domElement );
var controls = new OrbitControls( camera, renderer.domElement );

var loader = new GLTFLoader();

var obj;
loader.load("theme/static/huaranhuay/scene.gltf", function (gltf){
    obj = gltf.scene;
    scene.add(gltf.scene);
    
});



scene.background = new THREE.Color (0xd3d3d3);
var light = new THREE.HemisphereLight("white", "black", 2);
scene.add(light);
camera.position.set(3,7,5);



function animate(){
    requestAnimationFrame( animate );
    controls.update();
    renderer.render(scene, camera);
    }
animate();

var scale = 0;
function setScalar(score){
    scale += score;
}

function update() {
    // call the update() function every frame - creates a loop
    requestAnimationFrame(update);

    obj.rotation.y += 0.01;
    obj.scale.set(0.5+scale,0.5+scale,0.5+scale);
    obj.position.set(0,-2,0);
    
    // render the updated scene and camera
    renderer.render(scene, camera);
};
update();




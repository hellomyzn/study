using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GunManager : MonoBehaviour {

  public float bulletInterval;
  public GameObject audioControll;
  public RayControl raycontroll;
  public int bullet = 30;
  public int bulletBox = 150;
  int reloadBullet;
  RayControl raycontrollScript;
  AudioControl audioControllScript;

	// Use this for initialization
	void Start () {
		bulletInterval = 0;
		audioControllScript = audioControll.GetComponent<AudioControl>();
		raycontrollScript = raycontroll.GetComponent<RayControl>();
	}
	
	// Update is called once per frame
	void Update () {
		bulletInterval += Time.deltaTime;

		if(bullet <= 30 && bullet > 0){
			if(Input.GetMouseButtonDown(0)){
				Shot();			
			}else if(Input.GetMouseButtonUp(0) || Input.GetMouseButton(0)){
				raycontrollScript.DestroyBullet();
			}		
		}
		if(bullet < 30 && bullet >= 0){
			if(Input.GetKey(KeyCode.R)){
				reloadBullet = 30 - bullet;
				print(reloadBullet);
				bulletReload(reloadBullet);
			}
		}

	}

	void Shot(){
		if (bulletInterval >= 0.3f){
				bulletInterval = 0.0f;
				audioControllScript.GunShot();
				raycontrollScript.GenerateBullet();
				bullet --;
		}	
	}

	void bulletReload(int reloadBullet){
		if(bulletBox >= 30){
			bullet  =30;
			bulletBox = bulletBox - reloadBullet;
			print(bullet);
			print(bulletBox);
		}else if(bulletBox < 30 && bulletBox > 0){
			bullet += bulletBox;
			bulletBox = 0;
			print(bullet);
			print(bulletBox);
		}else{
			print("リロードできません");
			return;
		}
		audioControllScript.ReloadSound();
	}
}

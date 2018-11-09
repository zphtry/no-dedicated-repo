using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using UnityEngine;
using System.Collections;

namespace Assets.Scripts
{
    public class MainScript : MonoBehaviour
    {
        GameObject pla;

        // Use this for initialization
        void Start()
        {

        }

        // Update is called once per frame
        void Update()
        {



        }

        public void Exep()
        {
            //  pla = GameObject.Find("Spot1");

            //   pla.transform.position = new Vector3(pla.transform.position.x + 1, pla.transform.position.y, pla.transform.position.z);

            /* for (int i = 0; i < 5; i++)

                 Instantiate(GameObject.Find("Spot1"), new Vector3(10*i, 2*i, 0), new Quaternion(0, 0, 0, 0));  */

            GameObject pla = Instantiate(GameObject.Find("Spot1"));

            pla.transform.SetParent(GameObject.Find("Canvas").transform, false);

            pla.transform.localPosition = new Vector3(10, 10);
        }
    }
}
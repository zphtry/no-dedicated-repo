using UnityEngine;
using System.Collections;
using System.Collections.Generic;
using System;
using System.ComponentModel;
using System.Linq;
using System.Text;

public class GreySquareMoveScript : MonoBehaviour
{

    Transform spot, greySquare;

    Vector3 tmp;

    public void Swap()
    {
        spot = GetComponent<Transform>();

        greySquare = GameObject.Find("GreySquare").transform;

        tmp = greySquare.localPosition;

        greySquare.localPosition = spot.localPosition;

        spot.localPosition = tmp;

     //   spot.localPosition = GameObject.Find("GreySquare").transform.localPosition;
    }
}

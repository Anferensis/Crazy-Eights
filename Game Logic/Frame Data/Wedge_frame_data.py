
"""
Written by Albert "Anferensis" Ong

Loads all the frame data for a character.
"""

from bge import logic


def main():
    
    cont = logic.getCurrentController()
    owner = cont.owner
    
    owner["frame_data"] = { 
    
        "Neutral" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(2, 5), 
                "hitboxes" : ("04", ),
                
                "hitbox_data_04" : {
                
                    "damage" : 4,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.00,
                    
                    },                
                },                 
            },
        
            
        "Up Neutral" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(2, 9), 
                "hitboxes" : ("03", "04", ),


                "hitbox_data_03" : {
                
                    "damage" : 11,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    },
                                     
                "hitbox_data_04" : {
                
                    "damage" : 11,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    },                
                },                 
            },
            
            
        "Down Neutral" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(5, 9), 
                "hitboxes" : ("09", "10", ),
                
                "hitbox_data_09" : {
                
                    "damage" : 10,
                    "hitstun" : 0, 
                    "force_x" : 0.05, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    },
                    
                "hitbox_data_10" : {
                
                    "damage" : 10,
                    "hitstun" : 0, 
                    "force_x" : 0.05, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    },                  
                },                 
            },
        
            
        "Forward Neutral" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(4, 9), 
                "hitboxes" : ("09", "10"),
                
                "hitbox_data_09" : {
                
                    "damage" : 9,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    }, 
                    
                "hitbox_data_10" : {
                
                    "damage" : 9,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    },                
                },                 
            },
                     
                     
        "Up Jazz" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(10, 16), 
                "hitboxes" : ("08", "10", ),
                
                "hitbox_data_08" : {
                
                    "damage" : 18,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    }, 
                    
                "hitbox_data_10" : {
                
                    "damage" : 18,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    },                
                },                 
            },


        "Down Jazz" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(5, 11), 
                "hitboxes" : ("07", "08", "09", "10" ),
                
                "hitbox_data_07" : {
                
                    "damage" : 13,
                    "hitstun" : 0, 
                    "force_x" : 0.15, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    }, 
                    
                "hitbox_data_08" : {
                
                    "damage" : 13,
                    "hitstun" : 0, 
                    "force_x" : 0.15, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    },
                    
                "hitbox_data_09" : {
                
                    "damage" : 13,
                    "hitstun" : 0, 
                    "force_x" : 0.15, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    },
                    
                "hitbox_data_10" : {
                
                    "damage" : 13,
                    "hitstun" : 0, 
                    "force_x" : 0.15, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    },               
                },                 
            },
         
            
        "Forward Jazz" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(12, 18), 
                "hitboxes" : ("05", "06", ),
                
                "hitbox_data_05" : {
                
                    "damage" : 13,
                    "hitstun" : 0, 
                    "force_x" : 0.25, 
                    "force_z" : 0.10, 
                    "scaling" : 0.50,
                    
                    },  
                    
                "hitbox_data_06" : {
                
                    "damage" : 13,
                    "hitstun" : 0, 
                    "force_x" : 0.25, 
                    "force_z" : 0.10, 
                    "scaling" : 0.50,
                    
                    },              
                },                 
            },
            
            
        "Neutral Aerial" : { 
            
            "phases" : ("phase1", "phase2", ), 
                
            "phase1" : {
                
                "active_frames" : range(4, 9), 
                "hitboxes" : ("07", "08", "09", "10", ),
                
                "hitbox_data_07" : {
                
                    "damage" : 10,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    }, 
                    
                "hitbox_data_08" : {
                
                    "damage" : 10,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    }, 
                    
                "hitbox_data_09" : {
                
                    "damage" : 10,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    }, 
                    
                "hitbox_data_10" : {
                
                    "damage" : 10,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.50,
                    
                    },                
                },
                            
            "phase2" : {
                
                "active_frames" : range(9, 32), 
                "hitboxes" : ("07", "08", "09", "10", ),
                
                "hitbox_data_07" : {
                
                    "damage" : 8,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.25,
                    
                    }, 
                    
                "hitbox_data_08" : {
                
                    "damage" : 8,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.25,
                    
                    }, 
                    
                "hitbox_data_09" : {
                
                    "damage" : 8,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.25,
                    
                    }, 
                    
                "hitbox_data_10" : {
                
                    "damage" : 8,
                    "hitstun" : 0, 
                    "force_x" : 0.08, 
                    "force_z" : 0.15, 
                    "scaling" : 0.25,
                    
                    },                
                },                 
            },


        "Up Aerial" : { 
            
            "phases" : ("phase1", "phase2", ), 
                
            "phase1" : {
                
                "active_frames" : range(4, 9), 
                "hitboxes" : ("07", "08", ),
                
                "hitbox_data_07" : {
                
                    "damage" : 12,
                    "hitstun" : 0, 
                    "force_x" : 0.00, 
                    "force_z" : 0.10, 
                    "scaling" : 0.30,
                    
                    }, 
                    
                "hitbox_data_08" : {
                
                    "damage" : 12,
                    "hitstun" : 0, 
                    "force_x" : 0.00, 
                    "force_z" : 0.10, 
                    "scaling" : 0.30,
                    
                    },               
                }, 
                             
            "phase2" : {
                
                "active_frames" : range(9, 15), 
                "hitboxes" : ("07", "08", ),
                
                "hitbox_data_07" : {
                
                    "damage" : 9,
                    "hitstun" : 0, 
                    "force_x" : 0.00, 
                    "force_z" : 0.10, 
                    "scaling" : 0.15,
                    
                    }, 
                    
                "hitbox_data_08" : {
                
                    "damage" : 9,
                    "hitstun" : 0, 
                    "force_x" : 0.00, 
                    "force_z" : 0.10, 
                    "scaling" : 0.15,
                    
                    },               
                },                
            },


        "Down Aerial" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(15, 21), 
                "hitboxes" : ("07", "08", "09", "10", ),
                
                "hitbox_data_07" : {
                
                    "damage" : 16,
                    "hitstun" : 0, 
                    "force_x" : 0.00, 
                    "force_z" : -0.10, 
                    "scaling" : 0.40,
                    
                    },
                    
                "hitbox_data_08" : {
                
                    "damage" : 16,
                    "hitstun" : 0, 
                    "force_x" : 0.00, 
                    "force_z" : -0.10, 
                    "scaling" : 0.40,
                    
                    },
                    
                "hitbox_data_09" : {
                
                    "damage" : 16,
                    "hitstun" : 0, 
                    "force_x" : 0.00, 
                    "force_z" : -0.10, 
                    "scaling" : 0.40,
                    
                    },
                    
                "hitbox_data_10" : {
                
                    "damage" : 16,
                    "hitstun" : 0, 
                    "force_x" : 0.00, 
                    "force_z" : -0.10, 
                    "scaling" : 0.40,
                    
                    },                
                },                 
            },


        "Forward Aerial" : { 
            
            "phases" : ("phase1", "phase2", ), 
                
            "phase1" : {
                
                "active_frames" : range(3, 8), 
                "hitboxes" : ("07", "08", "09", "10", ),
                
                "hitbox_data_07" : {
                
                    "damage" : 12,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.30,
                    
                    }, 
                    
                "hitbox_data_08" : {
                
                    "damage" : 12,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.30,
                    
                    }, 

                "hitbox_data_09" : {
                
                    "damage" : 12,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.30,
                    
                    }, 
                    
                "hitbox_data_10" : {
                
                    "damage" : 12,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.30,
                    
                    },                
                },
             
                
            "phase2" : {
                
                "active_frames" : range(8, 19), 
                "hitboxes" : ("07", "08", "09", "10", ),
                
                "hitbox_data_07" : {
                
                    "damage" : 7,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    }, 
                    
                "hitbox_data_08" : {
                
                    "damage" : 7,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    }, 

                "hitbox_data_09" : {
                
                    "damage" : 7,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    }, 
                    
                "hitbox_data_10" : {
                
                    "damage" : 7,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    },                
                },                 
            },


        "Back Aerial" : { 
            
            "phases" : ("phase1", ), 
                
            "phase1" : {
                
                "active_frames" : range(8, 14), 
                "hitboxes" : ("07", "08", ),
                
                "hitbox_data_07" : {
                
                    "damage" : 10,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.10,
                    
                    }, 
                    
                "hitbox_data_08" : {
                
                    "damage" : 14,
                    "hitstun" : 0, 
                    "force_x" : 0.10, 
                    "force_z" : 0.10, 
                    "scaling" : 0.30,
                    
                    },               
                },                 
            },             
        }



#======================================================

main()



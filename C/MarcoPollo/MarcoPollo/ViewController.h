//
//  ViewController.h
//  MarcoPollo
//
//  Created by m garabedian on 4/4/16.
//  Copyright © 2016 m garabedian. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

- (IBAction)postItButtonPressed:(id)sender;
@property (weak, nonatomic) IBOutlet UITextField *tweetTextView;


@end

